import streamlit as st
import streamlit.components.v1 as components

# bootstrap 4 collapse example
def privacy():
    components.html(
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Privacy Policy</title>
    </head>
    <body>
      <h1>Privacy Policy</h1>
      <p>This Privacy Policy describes how we collect, use, and protect your personal data when you use our AI services.</p>

      <h2>1. Information We Collect</h2>
      <p>We may collect the following types of personal data:
          <ul>
              <li>Contact Information (e.g., name, email address)</li>
              <li>Usage Data (e.g., IP address, device information)</li>
              <li>Location Data (if permitted by your device settings)</li>
          </ul>
      </p>

      <h2>2. Use of Personal Data</h2>
      <p>We use your personal data for the following purposes:
          <ul>
              <li>To provide and maintain our AI services</li>
              <li>To improve and customize our services</li>
              <li>To communicate with you about our services</li>
              <li>To comply with legal obligations</li>
          </ul>
      </p>

      <h2>3. Data Sharing</h2>
      <p>We may share your personal data with third parties in the following situations:
          <ul>
              <li>With your consent</li>
              <li>For legal or regulatory purposes</li>
              <li>With service providers who assist us in providing our services</li>
          </ul>
      </p>

      <h2>4. Data Security</h2>
      <p>We take appropriate measures to protect your personal data from unauthorized access, alteration, disclosure, or destruction.</p>

      <h2>5. Your Rights</h2>
      <p>You have the following rights regarding your personal data:
          <ul>
              <li>Right to access</li>
              <li>Right to rectification</li>
              <li>Right to erasure</li>
              <li>Right to data portability</li>
              <li>Right to object</li>
          </ul>
      </p>

      <h2>6. Cookies and Tracking</h2>
      <p>We may use cookies and similar tracking technologies to enhance your experience and analyze usage patterns. You can manage your cookie preferences through your browser settings.</p>

      <h2>7. Changes to Privacy Policy</h2>
      <p>We reserve the right to update this Privacy Policy at any time. We will notify you of any changes by posting the new policy on this page.</p>

      <h2>8. Contact Us</h2>
      <p>If you have any questions or concerns about our Privacy Policy, please contact us at admin@aibyml.com.</p>

      <footer>
          <p>&copy; 2024 AIbyML.com. All rights reserved.</p>
      </footer>
    </body>
    </html>
    """,
    height = 1200
    )
  
