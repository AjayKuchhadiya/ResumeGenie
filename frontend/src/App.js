import React, { useState } from 'react';
import UploadForm from './components/UploadForm';
import DisplayData from './components/DisplayData';
import { uploadResume } from './services/api';
import { Container, Spinner, Alert, Row, Col } from 'react-bootstrap';

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
      setError("Error uploading file. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container className="mt-5">
      <h1 className="text-center mb-4">Resume Genie</h1>
      <Row className="justify-content-center">
        <Col md={6}>
          <UploadForm onUpload={handleUpload} />
        </Col>
      </Row>
      {loading && (
        <div className="text-center mt-4">
          <Spinner animation="border" variant="primary" />
        </div>
      )}
      {error && <Alert variant="danger" className="mt-4">{error}</Alert>}
      {data && <DisplayData data={data} />}
    </Container>
  );
}

export default App;
