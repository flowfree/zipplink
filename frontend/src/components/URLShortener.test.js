import { rest } from 'msw';
import { setupServer } from 'msw/node';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event'
import URLShortener from './URLShortener';
import '@testing-library/jest-dom'

const serverUrl = 'http://localhost:8000'

const server = setupServer(
  rest.post(`${serverUrl}/urls`, (req, res, ctx) => {
    return res(ctx.json({'short_url': `${serverUrl}/abcdef`}));
  })
);

beforeAll(() => server.listen())
afterEach(() => server.resetHandlers())
afterAll(() => server.close())

describe('URLShortener', () => {
  test('renders the component', () => {
    render(<URLShortener />);

    expect(screen.getByPlaceholderText("Paste your long URL")).toBeInTheDocument();
    expect(screen.getByRole('button')).toBeInTheDocument();
    expect(screen.getByRole('button')).toHaveTextContent('Shorten URL');
  });

  test('displays the short URL', async () => {
    render(<URLShortener />);

    let textfield = screen.getByPlaceholderText('Paste your long URL');
    userEvent.type(textfield, 'http://example.com/a/b/c/some-long-document.html');
    userEvent.click(screen.getByRole('button'));

    const helpText = await screen.findByRole('note')
    expect(helpText).toHaveTextContent('Press CTRL+C or CMD+C to copy your short URL.')
    
    textfield = screen.getByRole('textbox')
    expect(textfield).toHaveValue(`${serverUrl}/abcdef`)
  });

  test('validates the given input and displays error messages', async () => {
    server.use(
      rest.post(`${serverUrl}/urls`, (req, res, ctx) => {
        return res(
          ctx.status(400),
          ctx.json({'long_url': ['Please enter valid URL.']})
        );
      })
    );

    render(<URLShortener />);

    const textfield = screen.getByPlaceholderText('Paste your long URL');
    userEvent.type(textfield, 'http://example.com/a/b/c/some-long-document.html');
    userEvent.click(screen.getByRole('button'));

    const alert = await screen.findByRole('alert');
    expect(alert).toHaveTextContent('Please enter valid URL.');
  });
});
