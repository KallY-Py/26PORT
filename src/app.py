from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message
import logging
from datetime import datetime
import smtplib
import ssl

app = Flask(__name__)
CORS(app)

# Email Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587  # Changed from 465 to 587 for TLS
app.config['MAIL_USE_TLS'] = True  # Changed to True
app.config['MAIL_USE_SSL'] = False  # Changed to False
app.config['MAIL_USERNAME'] = 'jcporcopio03@gmail.com'
app.config['MAIL_PASSWORD'] = 'nwbl xprw ehum ojqn' 
app.config['MAIL_DEFAULT_SENDER'] = 'jcporcopio03@gmail.com'
app.config['MAIL_DEBUG'] = True

# Initialize Mail
mail = Mail(app)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@app.route('/api/send-message', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        logger.debug(f"Received data: {data}")
        
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        message = data.get('message', '').strip()
        
        if not name or not email or not message:
            return jsonify({
                'success': False,
                'message': 'All fields are required'
            }), 400
        
        if '@' not in email or '.' not in email:
            return jsonify({
                'success': False,
                'message': 'Please enter a valid email address'
            }), 400
        
        # Test connection first
        try:
            logger.info("Testing SMTP connection...")
            with smtplib.SMTP(app.config['MAIL_SERVER'], app.config['MAIL_PORT']) as server:
                server.starttls(context=ssl.create_default_context())
                server.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
                logger.info("SMTP connection successful")
        except Exception as e:
            logger.error(f"SMTP connection failed: {str(e)}")
            return jsonify({
                'success': False,
                'message': f'Email configuration error: {str(e)}'
            }), 500
        
        # Create email message to yourself
        msg = Message(
            subject=f"Portfolio Contact Form - Message from {name}",
            recipients=['jcporcopio03@gmail.com'],
            body=f"""
New message from your portfolio website!

───────────────────────────────────

Name: {name}
Email: {email}
Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

───────────────────────────────────
MESSAGE:
───────────────────────────────────

{message}

───────────────────────────────────

Reply to: {email}
            """,
            sender=app.config['MAIL_USERNAME']
        )
        
        # Send the email
        mail.send(msg)
        logger.info(f"Main email sent to jcporcopio03@gmail.com from {email}")
        
        # Optional: Send auto-reply to the user (skip if error to avoid double-failure)
        try:
            auto_reply = Message(
                subject="Thank you for contacting John Carl Porcopio!",
                recipients=[email],
                body=f"""
Dear {name},

Thank you for reaching out to me through my portfolio website!

I have received your message and will get back to you within 24 hours.

Here's a copy of your message for reference:
───────────────────────────────────
{message}
───────────────────────────────────

Best regards,
John Carl Porcopio
Junior Web Developer

───────────────────────────────────
Mobile: 09083277282
Email: jcporcopio03@gmail.com
GitHub: github.com/KallY-Py
───────────────────────────────────
                """
            )
            mail.send(auto_reply)
            logger.info(f"Auto-reply sent to {email}")
        except Exception as reply_error:
            logger.warning(f"Auto-reply failed (non-critical): {str(reply_error)}")
        
        return jsonify({
            'success': True,
            'message': 'Your message has been sent successfully! I will get back to you soon.'
        }), 200
        
    except Exception as e:
        logger.error(f"Error sending email: {str(e)}", exc_info=True)
        return jsonify({
            'success': False,
            'message': f'Failed to send message: {str(e)}'
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)