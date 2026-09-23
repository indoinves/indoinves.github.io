import React from 'react';

// Definisi tipe data (opsional jika ingin memperluas properti komponen)
interface IndoInvesHomeProps {
  appName?: string;
}

export default function IndoInvesHome({ appName = "IndoInves" }: IndoInvesHomeProps): React.JSX.Element {
  const currentYear: number = new Date().getFullYear();

  return (
    <div style={styles.body}>
      <div style={styles.container}>
        <img 
          src="https://indoinves.github.io/img/indoinves.png" 
          alt={`${appName} Logo`} 
          style={styles.logo} 
        />
        <h1 style={styles.h1}>Selamat Datang di {appName}</h1>
        <p style={styles.p}>
          Platform pintar investasi, keuangan, dan kumpulan tools finansial modern untuk membantu masa depan finansial Anda.
        </p>
        
        <div style={styles.btnGroup}>
          <a 
            href="https://indoinves.github.io/" 
            style={styles.btn}
            target="_blank" 
            rel="noopener noreferrer"
          >
            Buka Website Utama
          </a>
          <a 
            href="https://indoinves.github.io/tools/investasi.html" 
            style={{ ...styles.btn, ...styles.btnSecondary }}
            target="_blank" 
            rel="noopener noreferrer"
          >
            Jelajahi Tools
          </a>
        </div>

        <footer style={styles.footer}>
          &copy; {currentYear} {appName}. All rights reserved.
        </footer>
      </div>
    </div>
  );
}

// Objek gaya dengan tipe CSSProperties bawaan React
const styles: { [key: string]: React.CSSProperties } = {
  body: {
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif',
    backgroundColor: '#f8fafc',
    color: '#1e293b',
    lineHeight: 1.6,
    display: 'flex',
    flexDirection: 'column',
    minHeight: '100vh',
    justifyContent: 'center',
    alignItems: 'center',
    textAlign: 'center',
    padding: '20px',
    margin: 0,
  },
  container: {
    maxWidth: '600px',
    background: '#ffffff',
    padding: '40px',
    borderRadius: '12px',
    boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
  },
  logo: {
    width: '100px',
    height: '100px',
    marginBottom: '20px',
    borderRadius: '50%',
    objectFit: 'cover',
  },
  h1: {
    fontSize: '24px',
    marginBottom: '10px',
    color: '#0f172a',
  },
  p: {
    color: '#64748b',
    marginBottom: '25px',
  },
  btnGroup: {
    display: 'flex',
    gap: '10px',
    justifyContent: 'center',
    flexWrap: 'wrap',
  },
  btn: {
    display: 'inline-block',
    backgroundColor: '#2563eb',
    color: 'white',
    padding: '10px 20px',
    borderRadius: '6px',
    textDecoration: 'none',
    fontWeight: '600',
    transition: 'background-color 0.2s',
  },
  btnSecondary: {
    backgroundColor: '#e2e8f0',
    color: '#475569',
  },
  footer: {
    marginTop: '30px',
    fontSize: '14px',
    color: '#94a3b8',
  },
};
