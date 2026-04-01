/**
 * IMAP Client for reading emails
 */

const Imap = require('imap');
const { SimpleParser } = require('mailparser');

class IMAPClient {
  constructor(config) {
    this.imap = new Imap(config);
  }
  
  connect() {
    return new Promise((resolve, reject) => {
      this.imap.once('ready', () => resolve());
      this.imap.once('error', reject);
      this.imap.connect();
    });
  }
  
  getUnreadMessages() {
    return new Promise((resolve, reject) => {
      this.imap.openBox('INBOX', false, (err, box) => {
        if (err) return reject(err);
        
        this.imap.search(['UNSEEN'], (err, results) => {
          if (err) return reject(err);
          if (!results.length) return resolve([]);
          
          const messages = [];
          const fetch = this.imap.fetch(results, { bodies: '' });
          
          fetch.on('message', (msg, seqno) => {
            msg.on('body', (stream, info) => {
              SimpleParser(stream, (err, parsed) => {
                if (!err) messages.push(parsed);
              });
            });
          });
          
          fetch.once('end', () => resolve(messages));
          fetch.once('error', reject);
        });
      });
    });
  }
  
  disconnect() {
    this.imap.end();
  }
}

module.exports = IMAPClient;