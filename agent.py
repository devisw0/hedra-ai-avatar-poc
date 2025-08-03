# agent.py - SAFE TEST VERSION (No AI services, no credit consumption)
import asyncio
import os
from dotenv import load_dotenv
from PIL import Image

from livekit.agents import Agent, AgentSession, JobContext, WorkerOptions, cli
from livekit.plugins import hedra

load_dotenv()

async def entrypoint(ctx: JobContext):
    """SAFE TEST - No AI services, just connection testing"""
    print(f"🚀 SAFE TEST - New job started for room: {ctx.room.name}")
    
    # Wait for the first participant to join (this will be your client)
    await ctx.connect(auto_subscribe="audio_only")
    
    print(f"✅ Connected to room: {ctx.room.name}")
    print(f"👥 Current participants: {len(ctx.room.remote_participants)}")
    
    # Wait for a human participant to join
    participant = await ctx.wait_for_participant()
    print(f"👤 Human participant joined: {participant.identity}")
    
    # Load avatar image
    try:
        avatar_image = Image.open("robot_avatar.png")
        print("🖼️ Avatar image loaded successfully")
    except FileNotFoundError:
        print("❌ robot_avatar.png not found! Using default...")
        # Create a simple colored image as fallback
        avatar_image = Image.new('RGB', (512, 512), color='blue')
    
    # SAFE TEST: Create minimal agent session with NO AI services
    agent_session = AgentSession(
        ctx=ctx,
        identity=participant.identity,
        chat_manager=None,  # NO AI services
        vad=None,  # NO voice detection
        stt=None,  # NO speech-to-text
        llm=None,  # NO language model
        tts=None,  # NO text-to-speech
    )
    
    print("🤖 Starting SAFE agent session (no AI services)...")
    agent_session.start()
    
    # SAFE TEST: Simple agent with no AI
    agent = Agent(
        instructions="You are a test avatar. No AI processing."
    )
    
    print("🎭 Creating SAFE avatar session...")
    
    # Create and start avatar within the agent session
    avatar = hedra.AvatarSession(
        avatar_image=avatar_image,
        agent=agent,
    )
    
    print("⏳ Starting avatar (SAFE TEST - no AI)...")
    await avatar.start(room=ctx.room, agent_session=agent_session)
    
    print("✅ SAFE TEST: Avatar started successfully!")
    print("📹 Video track should now be visible to client")
    print("💡 NO AI services = NO credit consumption")
    print("🔍 This is just testing the connection")
    
    # Monitor for 30 seconds then auto-terminate
    print("⏰ SAFE TEST: Will auto-terminate in 30 seconds...")
    for i in range(30):
        await asyncio.sleep(1)
        if i % 10 == 0:
            print(f"⏱️ SAFE TEST: {30-i} seconds remaining...")
        
        # Check if client disconnected
        if len(ctx.room.remote_participants) == 0:
            print("⚠️ Client disconnected - ending test")
            break
    
    print("🔚 SAFE TEST: Auto-terminating (no credits consumed)")
    await avatar.aclose()
    agent_session.end()

if __name__ == "__main__":
    # Configure worker options
    worker_options = WorkerOptions(
        entrypoint_fnc=entrypoint,
        max_concurrent_jobs=1,
    )
    
    print("🚀 Starting SAFE LiveKit Agent Worker...")
    print("💡 NO AI services = NO credit consumption")
    print("🎯 Waiting for clients to connect...")
    print("⏰ Will auto-terminate after 30 seconds")
    
    cli.run_app(worker_options)
