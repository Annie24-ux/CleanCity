import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import Login from './Login';
import { useNavigate, useLocation } from 'react-router-dom';
import { login as authLogin, getCurrentUser } from '../services/authService';

jest.mock('react-router-dom', () => ({
  ...jest.requireActual('react-router-dom'),
  useNavigate: jest.fn(),
  useLocation: () => ({ state: null }),
}));

jest.mock('../services/authService', () => ({
  login: jest.fn((email, password) => ({ email })),
  getCurrentUser: jest.fn(() => null),
  logout: jest.fn(),
}));

describe('Login Component', () => {
  const mockNavigate = jest.fn();

  beforeEach(() => {
    jest.clearAllMocks();
    useNavigate.mockReturnValue(mockNavigate);
  });

  test('renders login form correctly', () => {
    render(<Login onLogin={jest.fn()} />);
    expect(screen.getByLabelText(/Email/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/Password/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /Login/i })).toBeInTheDocument();
  });

  test('shows error if fields are empty', () => {
    render(<Login onLogin={jest.fn()} />);
    fireEvent.click(screen.getByRole('button', { name: /Login/i }));
    expect(screen.getByRole('alert')).toHaveTextContent('Please enter email and password.');
  });

  test('calls login and onLogin on valid submit', () => {
    const mockOnLogin = jest.fn();
    render(<Login onLogin={mockOnLogin} />);

    fireEvent.change(screen.getByLabelText(/Email/i), {
      target: { value: 'test@example.com' },
    });
    fireEvent.change(screen.getByLabelText(/Password/i), {
      target: { value: 'password123' },
    });

    fireEvent.click(screen.getByRole('button', { name: /Login/i }));

    expect(authLogin).toHaveBeenCalledWith('test@example.com', 'password123');
    expect(mockOnLogin).toHaveBeenCalledWith({ email: 'test@example.com' });
    expect(mockNavigate).toHaveBeenCalledWith('/profile', { replace: true });
  });

  test('redirects to profile if already logged in', () => {
    getCurrentUser.mockReturnValueOnce({ email: 'already@logged.in' });

    render(<Login onLogin={jest.fn()} />);

    expect(mockNavigate).toHaveBeenCalledWith('/profile', { replace: true });
  });
});
