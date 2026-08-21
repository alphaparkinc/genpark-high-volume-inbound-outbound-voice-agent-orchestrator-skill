from client import HighVolumeInboundOutboundVoiceAgentOrchestratorClient

def main():
    client = HighVolumeInboundOutboundVoiceAgentOrchestratorClient()
    script = "Hello, this is Nova from Flowmatic. I'm calling to follow up on your recent trial sign-up..."
    res = client.handle_call(script, "+14155552671")
    print(f"Outcome: {res['outcome']}")
    print(f"Warm Transfer: {res['warm_transfer_triggered']}")
    print(f"Summary: {res['call_transcript_summary']}")
    print("CRM Synced:", res["crm_fields_synced"])

if __name__ == "__main__":
    main()
