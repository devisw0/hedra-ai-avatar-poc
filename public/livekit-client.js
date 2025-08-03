// Minimal LiveKit Client for Avatar Demo
window.Livekit = {
  Room: class Room {
    constructor() {
      this.onTrackSubscribed = null;
      this.onConnected = null;
      this.onDisconnected = null;
      this.tracks = new Map();
    }

    async connect(url, token) {
      console.log('Connecting to LiveKit server...');
      console.log('URL:', url);
      console.log('Token:', token.substring(0, 50) + '...');
      
      // Simulate connection delay
      await new Promise(resolve => setTimeout(resolve, 1000));
      
      // Create a mock video track that shows the agent is connected
      const mockTrack = {
        kind: 'video',
        attach: (element) => {
          console.log('Attaching video track to element');
          
          // Create a canvas with the robot avatar
          const canvas = document.createElement('canvas');
          canvas.width = 640;
          canvas.height = 480;
          const ctx = canvas.getContext('2d');
          
          // Draw background
          ctx.fillStyle = '#333';
          ctx.fillRect(0, 0, 640, 480);
          
          // Draw robot avatar
          ctx.fillStyle = '#0f0';
          ctx.font = '48px Arial';
          ctx.textAlign = 'center';
          ctx.fillText('🤖', 320, 200);
          
          // Draw status text
          ctx.fillStyle = '#fff';
          ctx.font = '24px Arial';
          ctx.fillText('Agent Connected!', 320, 240);
          ctx.fillText('Speak to interact...', 320, 270);
          
          // Add a pulsing effect to show it's active
          let pulse = 0;
          setInterval(() => {
            pulse = (pulse + 1) % 60;
            const alpha = 0.5 + 0.5 * Math.sin(pulse * 0.1);
            ctx.fillStyle = `rgba(0, 255, 0, ${alpha})`;
            ctx.fillText('🤖', 320, 200);
          }, 100);
          
          // Convert canvas to video stream
          const stream = canvas.captureStream(30);
          element.srcObject = stream;
          element.play();
        }
      };
      
      if (this.onTrackSubscribed) {
        this.onTrackSubscribed(mockTrack);
      }
      
      if (this.onConnected) {
        this.onConnected();
      }
      
      console.log('Connected to LiveKit room');
    }
  }
};