# agent.py
import asyncio
import os
from dotenv import load_dotenv
from PIL import Image

from livekit.agents import Agent, AgentSession, JobContext, WorkerOptions, cli
from livekit.plugins import openai, elevenlabs, silero, hedra

load_dotenv()

async def entrypoint(ctx: JobContext):
    await ctx.connect()
    print("🚀 Connected to LiveKit room!")

    avatar_image = Image.open("robot_avatar.png")  # Add your face image here

    # Define your agent's personality
    agent = Agent(
        instructions=(
            "You're a friendly AI assistant. Answer questions clearly and naturally. "
            "Keep it conversational."
        )
    )

    # Set up the brain (AI + voice)
    session = AgentSession(
        vad=silero.VAD.load(),  # Detect when user speaks
        stt=openai.STT(model="whisper-1"),
        llm=openai.LLM(model="gpt-4o"),
        tts=elevenlabs.TTS(model="eleven_turbo_v2_5"),
    )

    # Hedra Avatar = live video stream
    avatar = hedra.AvatarSession(avatar_image=avatar_image)

    await avatar.start(session, room=ctx.room)
    await session.start(agent=agent, room=ctx.room)

    await session.generate_reply(instructions="Say hello and ask how you can help.")

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
