# Netlify Dashboard Settings

## Fill in these fields in Netlify Dashboard:

### Branch to deploy
```
main
```

### Base directory
```
. 
```
*(Leave empty or just use a dot)*

### Build command
```
echo "Build complete"
```
*(Or leave empty - Netlify will use netlify.toml)*

### Publish directory
```
.
```
*(Leave empty or just use a dot)*

### Functions directory
```
netlify/functions
```

---

## ⚠️ Important Warning

**Netlify Functions may NOT work well for this project because:**

1. **TensorFlow is too large** (~500MB+)
   - Lambda limit: 250MB unzipped
   - Your model + TensorFlow will exceed this

2. **Cold start times** will be 10-30 seconds
   - Users will wait a long time for first prediction

3. **Memory limits** may be insufficient for TensorFlow

## ✅ Better Alternatives

### Option 1: Render (Easiest & Recommended)
1. Go to [render.com](https://render.com)
2. Connect GitHub
3. Create "Web Service"
4. Settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app --bind 0.0.0.0:$PORT`
   - Add `gunicorn` to requirements.txt

### Option 2: Railway (Very Easy)
1. Go to [railway.app](https://railway.app)
2. Connect GitHub
3. Deploy - it auto-detects Flask!

### Option 3: Heroku (Traditional)
1. Add `Procfile`: `web: gunicorn app:app`
2. Deploy via Heroku CLI or GitHub

---

## If You Still Want to Try Netlify:

1. Use the settings above
2. Add environment variable: `PYTHON_VERSION=3.9`
3. Deploy and monitor for errors
4. If it fails, switch to Render or Railway

