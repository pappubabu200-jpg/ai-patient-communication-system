# Project Prerequisites

This project requires the following before it can be run or deployed:

## Accounts & API Keys
- **OpenAI / ChatGPT API key** (for AI intent classification)
- **Twilio API key** (for WhatsApp and SMS)
- **SendGrid / Mailgun API key** (for email sending)
- **Make.com account** (for scenario automation)

## Environment Setup
1. Python 3.9+ installed
2. Install required packages:
   ```bash
   pip install fastapi uvicorn openai requests python-dotenv
   ```
3. Set environment variables (or fill `config/api_keys_placeholder.txt`):
   ```
   OPENAI_API_KEY=your_openai_api_key
   TWILIO_API_KEY=your_twilio_api_key
   SENDGRID_API_KEY=your_sendgrid_api_key
   ```

## Test Data
- `data/sample_patient_data.csv` contains placeholder patient messages for testing AI flows.

## Notes
- This project is a prototype. Replace all placeholder functions with actual logic before production.
- Ensure you follow healthcare compliance (HIPAA/GDPR) when using real patient data.
