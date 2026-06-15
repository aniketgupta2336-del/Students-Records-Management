# srm/utils/email_util.py

from django.core.mail import EmailMessage
from django.conf import settings


def send_confirmation_email(student_name, student_email, roll=None, course=None, contact=None):
    """
    Sends a professional HTML confirmation email to a student after saving their record.
    """

    if not student_email:
        print("❌ No email provided for", student_name)
        return False

    subject = f"✅ Student Record Confirmation for {student_name}"

    body = f"""
    <html>
      <body style="font-family: Arial, sans-serif; background-color:#f4f4f4; padding:20px;">

        <div style="max-width:600px; margin:0 auto; background:#fff; padding:20px;
                    border-radius:10px; box-shadow:0 0 10px rgba(0,0,0,0.1);">

          <h2 style="color:#2E86C1; text-align:center;">🎓 Student Record Saved</h2>

          <p style="font-size:16px; color:#333;">Hello <b>{student_name}</b>,</p>

          <p style="font-size:15px; color:#555;">
            Your student record has been successfully saved in our system. Below are the details:
          </p>

          <table style="width:100%; border-collapse: collapse; margin:20px 0;">
            <tr style="background:#2E86C1; color:#fff;">
              <th style="padding:10px; text-align:left;">Field</th>
              <th style="padding:10px; text-align:left;">Value</th>
            </tr>
            <tr>
              <td style="padding:10px; border:1px solid #ddd;">Roll No</td>
              <td style="padding:10px; border:1px solid #ddd;">{roll}</td>
            </tr>
            <tr>
              <td style="padding:10px; border:1px solid #ddd;">Course</td>
              <td style="padding:10px; border:1px solid #ddd;">{course}</td>
            </tr>
            <tr>
              <td style="padding:10px; border:1px solid #ddd;">Contact</td>
              <td style="padding:10px; border:1px solid #ddd;">{contact}</td>
            </tr>
          </table>

          <p style="font-size:15px; color:#555;">
            If any detail is incorrect, please contact the admin immediately.
          </p>

          <div style="margin-top:30px; text-align:center;">
            <p style="color:#777; font-size:13px;">
              Thanks,<br>
              <b>Student Records Management Team</b>
            </p>
          </div>

        </div>

      </body>
    </html>
    """

    try:
        email = EmailMessage(
            subject=subject,
            body=body,
            from_email=settings.EMAIL_HOST_USER,
            to=[student_email],
        )
        email.content_subtype = "html"   # 👉 important for HTML mails
        email.send(fail_silently=False)
        print(f"✅ Confirmation email sent to {student_email}")
        return True

    except Exception as e:
        print(f"❌ Error sending email to {student_email}:", e)
        return False
