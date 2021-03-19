import { useState } from 'react'

export default function URLShortener() {
  const [url, setUrl] = useState('https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html')

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
            onChange={e => setUrl(e.target.value)}
            className="form-control form-control-lg"
            placeholder="Paste your long URL"
          />
          <button 
            className="btn btn-primary"
            onClick={handleShortenUrl}
          >Shorten URL</button>
        </div>
      </form>
    </div>
  )
}
