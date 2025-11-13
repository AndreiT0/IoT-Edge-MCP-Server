#!/usr/bin/env python3
"""Blender MCP Chat - Come filesystem MCP"""
import asyncio
import sys
from pathlib import Path
from polymcp.polyagent import UnifiedPolyAgent, OllamaProvider

async def main():
    llm = OllamaProvider(model="kimi-k2-thinking:cloud", temperature=0)
    
    # Invece di stdio, usiamo HTTP endpoint
    mcp_servers = ["http://localhost:8000/mcp"]
    
    agent = UnifiedPolyAgent(
        llm_provider=llm, 
        mcp_servers=mcp_servers,  
        verbose=True
    )
    
    async with agent:
        print("✅ IoT MCP Server connected!\n")
        
        # Chat loop
        while True:
            user_input = input("\n🏭 You: ")
            
            if user_input.lower() in ['exit', 'quit']:
                print("Arrivederci!")
                break
            
            result = await agent.run_async(user_input, max_steps=5)
            print(f"\n🤖 System: {result}")

if __name__ == "__main__":
    asyncio.run(main())


'''
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
paho-mqtt==1.6.1
pymodbus==3.5.2
redis==5.0.1
influxdb-client==1.38.0
pyyaml==6.0.1
docstring-parser==0.15
python-multipart==0.0.6
pyserial==3.5  # per Modbus RTU
'''