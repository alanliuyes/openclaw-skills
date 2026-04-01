/**
 * SMTP Client for sending emails
 */

const nodemailer = require('nodemailer');

class SMTPClient {
  constructor(config) {
    this.transporter = nodemailer.createTransport(config);
  }
  
  async sendEmail(to, subject, text, html = null) {
    const mailOptions = {
      from: this.transporter.options.auth.user,
      to,
      subject,
      text,
      html: html || text
    };
    
    return await this.transporter.sendMail(mailOptions);
  }
  
  async verify() {
    return await this.transporter.verify();
  }
}

module.exports = SMTPClient;