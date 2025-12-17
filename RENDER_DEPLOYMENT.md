# Render Deployment Guide

## 🚀 Quick Start

Render is perfect for Flask + TensorFlow applications! Follow these steps:

## Step 1: Create Render Account

1. Go to [render.com](https://render.com)
2. Sign up with GitHub (recommended)
3. Connect your GitHub account

## Step 2: Create New Web Service

1. Click **"New +"** → **"Web Service"**
2. Connect your repository: `SrinivasSurisetti/traffic_sign_recognition`
3. Select branch: `main`

## Step 3: Configure Settings

Fill in these settings in the Render dashboard:

### Basic Settings

- **Name:** `traffic-sign-recognition` (or any name you prefer)
- **Region:** Choose closest to you (e.g., `Oregon (US West)`)
- **Branch:** `main`
- **Root Directory:** `.` (leave empty or use dot)

### Build & Deploy

- **Runtime:** `Python 3`
- **Build Command:** 
  ```
  pip install -r requirements.txt
  ```
- **Start Command:**
  ```
  gunicorn app:app --bind 0.0.0.0:$PORT
  ```

### Advanced Settings (Optional)

- **Plan:** `Starter` (Free tier) or `Standard` (for better performance)
- **Auto-Deploy:** `Yes` (deploys automatically on git push)

## Step 4: Environment Variables (Optional)

You can add these if needed:
- `PYTHON_VERSION=3.9.18`
- `PORT=10000` (Render sets this automatically)

## Step 5: Deploy!

1. Click **"Create Web Service"**
2. Render will:
   - Install dependencies from `requirements.txt`
   - Build your application
   - Deploy it
3. Wait 5-10 minutes for first deployment (TensorFlow installation takes time)

## Step 6: Access Your App

Once deployed, you'll get a URL like:
```
https://traffic-sign-recognition.onrender.com
```

## ✅ What's Already Configured

Your project is ready with:
- ✅ `Procfile` - Tells Render how to start the app
- ✅ `render.yaml` - Alternative configuration file
- ✅ `requirements.txt` - Includes `gunicorn` for production
- ✅ `app.py` - Updated to use PORT environment variable

## 📋 Files Created

1. **Procfile** - Production server command
2. **render.yaml** - Render configuration (optional, can use dashboard instead)
3. **requirements.txt** - Updated with `gunicorn` and `opencv-python-headless`

## 🔧 Troubleshooting

### Issue: Build fails with "opencv-python"
- **Solution:** Already fixed! Using `opencv-python-headless` instead

### Issue: App crashes on startup
- **Check:** Make sure `model.h5` is in the repository
- **Check:** Verify all dependencies are in `requirements.txt`

### Issue: Slow first request
- **Normal:** First request loads the model (10-30 seconds)
- **Solution:** Use Render's "Standard" plan for better performance

### Issue: Memory limit exceeded
- **Solution:** Upgrade to "Standard" plan (2GB RAM) or "Pro" plan

### Issue: Timeout errors
- **Solution:** Render free tier has 30-second timeout
- **Upgrade:** Use "Standard" plan for longer timeouts

## 💰 Pricing

- **Free Tier:** 
  - 750 hours/month
  - Spins down after 15 minutes of inactivity
  - 512MB RAM
  - Good for testing

- **Starter ($7/month):**
  - Always on
  - 512MB RAM
  - Better for production

- **Standard ($25/month):**
  - Always on
  - 2GB RAM
  - Recommended for ML apps

## 🎯 Next Steps After Deployment

1. **Test your app** at the provided URL
2. **Custom domain** (optional): Add your own domain in Render settings
3. **Monitor logs:** Check Render dashboard for any errors
4. **Set up auto-deploy:** Already enabled by default

## 📝 Notes

- First deployment takes 5-10 minutes (TensorFlow installation)
- Free tier apps spin down after inactivity (first request after spin-down takes ~30 seconds)
- Model file (`model.h5`) is included in the repository
- All static files and templates are included

## 🎉 Success!

Your Traffic Sign Recognition app should now be live on Render!

Visit your app URL and test uploading a traffic sign image.

