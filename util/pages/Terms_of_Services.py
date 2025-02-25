import streamlit as st
import streamlit.components.v1 as components

def tos():
    components.html(
      """
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Terms of Service</title>
      </head>
      <body>
          <h1>Terms of Service</h1>
            <p>Welcome to our AI Services! Please read these terms carefully before using our services.</p>
               <h2>1. Acceptance of Terms</h2>
                <p>By accessing or using our AI services, you agree to comply with these terms and conditions. If you do not agree with any part of these terms, you may not use our services.</p>
        
              <h2>2. Use of Services</h2>
                <p>Our AI services are provided for informational and educational purposes only. You may not use our services for any illegal or unauthorized purpose.</p>
          
              <h2>3. Data Privacy</h2>
                <p>We are committed to protecting your privacy. By using our AI services, you agree to our Privacy Policy, which outlines how we collect, use, and protect your data.</p>
          
              <h2>4. Intellectual Property</h2>
                <p>All content and materials provided through our AI services, including but not limited to text, graphics, logos, and software, are the property of our company or its licensors and are protected by intellectual property laws.</p>
          
              <h2>5. Limitation of Liability</h2>
                <p>We make no warranties or representations about the accuracy or reliability of our AI services. In no event shall we be liable for any direct, indirect, incidental, special, or consequential damages arising out of or in connection with your use of our services.</p>
          
              <h2>6. Changes to Terms</h2>
                <p>We reserve the right to modify or update these terms of service at any time. It is your responsibility to check this page periodically for changes. Your continued use of our services after any modifications indicates your acceptance of the updated terms.</p>
          
              <h2>7. Contact Us</h2>
                <p>If you have any questions or concerns about these terms, please contact us at admin@aibyml.com.</p>
        
          <footer>
              <p>&copy; 2024 AIbyML.com. All rights reserved.</p>
          </footer>
      </body>
      </html>
    """,
      height = 900
    )
