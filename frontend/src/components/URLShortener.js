import { useState, useRef, useEffect } from 'react'

export default function URLShortener() {
  const [url, setUrl] = useState('https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html')
  const [helpText, setHelpText] = useState('')
  const urlInput = useRef(null)

  useEffect(() => {
    if (url.startsWith('https://zipp.link')) {
      urlInput.current.select()
      setHelpText('Press CTRL+C to copy your short URL.')
    } else {
      setHelpText('')
    }
  }, [url])

  function handleShortenUrl(e) {
    e.preventDefault()
    setUrl('https://zipp.link/ax1eb')
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

        <div className="form-text">{helpText}</div>

      </form>
    </div>
  )
}
