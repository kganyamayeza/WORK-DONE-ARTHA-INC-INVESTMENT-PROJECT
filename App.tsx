import React from 'react';
import { Routes, Route } from 'react-router-dom';
import { ThemeProvider, createTheme, CssBaseline } from '@mui/material';
import Dashboard from './pages/Dashboard';
import Login from './pages/Login';
import Layout from './components/Layout';
import { useSelector } from 'react-redux';
import { RootState } from './store';

const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2',
      light: '#42a5f5',
      dark: '#1565c0',
    },
    secondary: {
      main: '#9c27b0',
      light: '#ba68c8',
      dark: '#7b1fa2',
    },
    background: {
      default: '#f5f5f5',
      paper: '#ffffff',
    },
  },
});

const App: React.FC = () => {
  const isAuthenticated = useSelector((state: RootState) => state.auth.isAuthenticated);

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route
          path="/*"
          element={
            isAuthenticated ? (
              <Layout>
                <Routes>
                  <Route path="/" element={<Dashboard />} />
                </Routes>
              </Layout>
            ) : (
              <Login />
            )
          }
        />
      </Routes>
    </ThemeProvider>
  );
};

export default App; 