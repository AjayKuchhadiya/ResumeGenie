import React, { useState } from 'react';
import { Button, Form } from 'react-bootstrap';

const UploadForm = ({ onUpload }) => {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (file) {
      onUpload(file);
    }
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group controlId="formFile" className="mb-3">
        <Form.Label>Select Resume (PDF or DOCX)</Form.Label>
        <Form.Control type="file" accept=".pdf,.docx" onChange={handleFileChange} />
      </Form.Group>
      <Button variant="primary" type="submit" disabled={!file} block>
        Upload Resume
      </Button>
    </Form>
  );
};

export default UploadForm;
