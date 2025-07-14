import React from 'react';
import { render, screen } from '@testing-library/react';
import LandingPage from './LandingPage';
import { BrowserRouter } from 'react-router-dom';

const renderWithRouter = (ui) => {
  return render(<BrowserRouter>{ui}</BrowserRouter>);
};

describe('LandingPage Component', () => {
  beforeEach(() => {
    renderWithRouter(<LandingPage />);
  });

  test('renders main title', () => {
    expect(screen.getByText(/Waste Pickup Scheduler/i)).toBeInTheDocument();
  });

  test('renders tagline', () => {
    expect(screen.getByText(/Cleaner streets, greener future/i)).toBeInTheDocument();
  });

  test('renders feature titles', () => {
    expect(screen.getByText('Easy Scheduling')).toBeInTheDocument();
    expect(screen.getByText('Dashboard')).toBeInTheDocument();
    expect(screen.getByText('Blog & Community')).toBeInTheDocument();
  });

  test('renders CTA buttons with correct links', () => {
    expect(screen.getByText('Sign Up').closest('a')).toHaveAttribute('href', '/register');
    expect(screen.getByText('Schedule Pickup').closest('a')).toHaveAttribute('href', '/home');
    expect(screen.getByText('Read Blog').closest('a')).toHaveAttribute('href', '/blog');
  });

  test('renders user testimonials', () => {
    expect(screen.getByText(/CleanCity made waste pickup so easy/i)).toBeInTheDocument();
    expect(screen.getByText(/Our neighborhood is cleaner and greener/i)).toBeInTheDocument();
    expect(screen.getByText(/Love the dashboard and the community/i)).toBeInTheDocument();
  });

  test('renders logo with CleanCity text', () => {
    expect(screen.getByText(/CleanCity/)).toBeInTheDocument();
  });
});
