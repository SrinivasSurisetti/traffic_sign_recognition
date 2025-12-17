# Netlify Deployment Guide

## ⚠️ Important Note

**Netlify Functions have limitations for heavy ML applications:**
- Lambda function size limit: 250MB unzipped
- Memory limit: Up to 10GB (but costs increase)
- Cold start times can be 10-30 seconds with TensorFlow
- Timeout limit: 10 seconds (can be extended to 26 seconds)

**Recommended Alternatives:**
- **Render** (render.com) - Better for Flask + ML apps
- **Railway** (railway.app) - Easy deployment
- **Heroku** - Traditional but reliable
- **AWS Elastic Beanstalk** - Full control

## Netlify Configuration

### Dashboard Settings

Fill in the Netlify dashboard with these values:

#### Branch to deploy
```
main
```

#### Base directory
```
. (leave empty or use dot)
```

#### Build command
```
echo "No build step required"
```
*Or leave empty*

#### Publish directory
```
. (leave empty or use dot)
```

#### Functions directory
```
netlify/functions
```

### Environment Variables (Optional but Recommended)

Add these in Netlify dashboard under "Environment variables":

```
PYTHON_VERSION=3.9
```

### File Structure

The deployment uses:
- `netlify.toml` - Configuration file
- `netlify/functions/app.py` - Serverless function wrapper
- `netlify/functions/requirements.txt` - Function dependencies

## Deployment Steps

1. **Push to GitHub** (already done ✅)

2. **Connect to Netlify:**
   - Go to Netlify dashboard
   - Click "Add new site" → "Import an existing project"
   - Connect to GitHub
   - Select your repository: `SrinivasSurisetti/traffic_sign_recognition`
   - Use the settings above

3. **Deploy:**
   - Netlify will automatically detect `netlify.toml`
   - It will install dependencies
   - Deploy your site

## Potential Issues & Solutions

### Issue: Function timeout
- **Solution:** Increase timeout in `netlify.toml` or use a lighter model

### Issue: Package too large
- **Solution:** 
  - Use TensorFlow Lite instead of full TensorFlow
  - Optimize model size
  - Consider using external model hosting

### Issue: Cold starts too slow
- **Solution:** 
  - Use Netlify's "Background Functions" for longer execution
  - Consider keeping function warm with scheduled pings
  - Use a dedicated hosting service instead

## Alternative: Better Deployment Options

### Option 1: Render (Recommended)

1. Create account at render.com
2. Connect GitHub repository
3. Create new "Web Service"
4. Settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Environment:** Python 3

### Option 2: Railway

1. Create account at railway.app
2. Connect GitHub
3. Deploy from repository
4. Railway auto-detects Flask apps

### Option 3: Heroku

1. Create `Procfile`: `web: gunicorn app:app`
2. Update requirements.txt
3. Deploy via Heroku CLI or GitHub integration

## Testing Locally

To test Netlify Functions locally:

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Run locally
netlify dev
```

## Current Configuration

Your project is configured with:
- ✅ `netlify.toml` - Netlify configuration
- ✅ `netlify/functions/app.py` - Serverless wrapper
- ✅ `netlify/functions/requirements.txt` - Function dependencies

## Next Steps

1. **Try Netlify deployment** with the settings above
2. **If it fails** (likely due to TensorFlow size), consider:
   - Using Render or Railway instead
   - Optimizing the model (TensorFlow Lite)
   - Using a separate API service for predictions

