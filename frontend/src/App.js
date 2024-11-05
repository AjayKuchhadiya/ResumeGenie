import React, { useState } from 'react';
import UploadForm from './components/UploadForm';
import DisplayData from './components/DisplayData';
import { uploadResume } from './services/api';  

function App() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async (file) => {
    setLoading(true);
    setError(null);

    try {
      const response = await uploadResume(file);
      setData(response);
    } catch (err) {
      setError(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Resume Parser</h1>
      <UploadForm onUpload={handleUpload} />
      {loading && <p>Loading...</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {data && <DisplayData data={data} />}
    </div>
  );
}

export default App;
