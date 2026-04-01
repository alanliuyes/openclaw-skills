/**
 * Email Configuration Module
 */

const config = {
  providers: {
    gmail: {
      imap: { host: 'imap.gmail.com', port: 993, secure: true },
      smtp: { host: 'smtp.gmail.com', port: 587, secure: false }
    },
    outlook: {
      imap: { host: 'outlook.office365.com', port: 993, secure: true },
      smtp: { host: 'smtp.office365.com', port: 587, secure: false }
    },
    '163': {
      imap: { host: 'imap.163.com', port: 993, secure: true },
      smtp: { host: 'smtp.163.com', port: 587, secure: false }
    }
  },
  
  getProvider(name) {
    return this.providers[name.toLowerCase()] || null;
  }
};

module.exports = config;