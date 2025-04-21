import jsPDF from 'jspdf';
import html2canvas from 'html2canvas';

export async function exportCertificatePdf(elementId, filename = 'certificate.pdf') {
  const input = document.getElementById(elementId);
  const canvas = await html2canvas(input, { scale: 2 });
  const imgData = canvas.toDataURL('image/png');
  const pdf = new jsPDF({
    orientation: 'landscape',
    unit: 'px',
    format: [canvas.width, canvas.height]
  });
  pdf.addImage(imgData, 'PNG', 0, 0, canvas.width, canvas.height);
  pdf.save(filename);
}
