import axios from 'axios'
import { useEffect, useState, useRef } from 'react'

export default function URLShortener() {
  const [isMounted, setIsMounted] = useState(false)
  const [url, setUrl] = useState('')
  const [helpText, setHelpText] = useState('')
  const [error, setError] = useState('')
  const urlInput = useRef(null)

  useEffect(() => {
    setIsMounted(true)
    setHelpText('')
    if (url.startsWith('http://localhost') || url.startsWith('https://zipp.link')) {
      urlInput.current.select()
      setHelpText('Press CTRL+C or CMD+C to copy your short URL.')
    }
    return () => {
      setIsMounted(false)
    }
  }, [url])

  function handleShortenUrl(e) {
    e.preventDefault()
    const serverUrl = 'http://localhost:8000'
    axios
      .post(`${serverUrl}/urls`, { long_url: url })
      .then(response => {
        if (isMounted) {
          setUrl(response.data.short_url);
          setError('');
        }
      })
      .catch(error => {
        if (error.response.data && error.response.data.long_url && isMounted) {
          setError(error.response.data.long_url)
        }
      });
  }

  return (
    <div>
      <h1>Shorten Your URL</h1>
      <form action="" className="form" onSubmit={handleShortenUrl}>
        <div className="input-group mt-3">
          <input 
            type="text" 
            name="url" 
            value={url}
            ref={urlInput}
            onChange={e => setUrl(e.target.value)}
            className="form-control form-control-lg shadow-none"
            placeholder="Paste your long URL"
          />
          <button 
            className="btn btn-primary"
            onClick={handleShortenUrl}
          >
            Shorten URL
          </button>
        </div>

        {helpText && (
          <div className="form-text text-muted" role="note">{helpText}</div>
        )}

        {error && (
          <div className="alert alert-danger alert-dismissible text-start mt-3" role="alert">
            <strong>Heads up!</strong> {error}
            <button type="button" className="btn-close" data-bs-dismiss="alert" onClick={() => setError('')}></button>
          </div>
        )}

      </form>
    </div>
  )
}
