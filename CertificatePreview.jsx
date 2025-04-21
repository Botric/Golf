import React from 'react';
import './CertificatePreview.css';
import golferSilhouette from './golfer-silhouette-1.png';

export default function CertificatePreview({ name, date, signature }) {
  return (
    <div className="certificate-container">
      <img src={golferSilhouette} alt="Golfer" className="certificate-golfer" />
      <div className="certificate-title">CERTIFICATE</div>
      <div className="certificate-subtitle">OF APPRECIATION</div>
      <div className="certificate-awarded">AWARDED TO</div>
      <div className="certificate-name">{name}</div>
      <div style={{ textAlign: 'center', color: '#888', margin: '20px 0' }}>
        {/* Optional: Add a short description or leave blank */}
        {/* "For outstanding performance and dedication." */}
      </div>
      <div className="certificate-footer">
        <div>
          <div className="certificate-date-sign">{date}</div>
          DATE
        </div>
        <div>
          <div className="certificate-date-sign">{signature}</div>
          SIGNATURE
        </div>
      </div>
    </div>
  );
}
