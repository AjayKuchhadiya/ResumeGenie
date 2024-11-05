import axios from 'axios';

const API_BASE_URL = "http://127.0.0.1:8000";

export const uploadResume = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await axios.post(`${API_BASE_URL}/upload/`, formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    });
    return response.data;
  } catch (error) {
    throw error.response ? error.response.data.detail : "An error occurred";
  }
};
