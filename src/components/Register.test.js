import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import Register from './Register';

describe('Register Component', () => {
  test('renders form fields', () => {
    render(<Register />, {});

    expect(screen.getByLabelText(/Name/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/Email/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/Password/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /Register/i })).toBeInTheDocument();
  });

  test('shows error when fields are empty', () => {
    render(<Register />);

    fireEvent.click(screen.getByRole('button', { name: /Register/i }));
    expect(screen.getByRole('alert')).toHaveTextContent('Please fill in all fields.');
  });

  test('calls onRegister with valid input', () => {
    const mockRegister = jest.fn();
    render(<Register onRegister={mockRegister} />);

    fireEvent.change(screen.getByLabelText(/Name/i), {
      target: { value: 'John Doe' },
    });
    fireEvent.change(screen.getByLabelText(/Email/i), {
      target: { value: 'john@example.com' },
    });
    fireEvent.change(screen.getByLabelText(/Password/i), {
      target: { value: 'securepass123' },
    });

    fireEvent.click(screen.getByRole('button', { name: /Register/i }));

    expect(mockRegister).toHaveBeenCalledWith({
      name: 'John Doe',
      email: 'john@example.com',
    });
  });
});
