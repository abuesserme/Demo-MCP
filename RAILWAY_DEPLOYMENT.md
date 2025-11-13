# Railway Deployment Guide

## Quick Deploy (Recommended)

### Method 1: Deploy from GitHub

1. **Push your code to GitHub** (if not already):
```bash
git add .
git commit -m "Prepare for Railway deployment"
git push origin main
```

2. **Deploy on Railway**:
   - Go to [railway.app](https://railway.app)
   - Click "Start a New Project"
   - Click "Deploy from GitHub repo"
   - Select your repository
   - Railway will auto-detect it's a Python app and deploy!

3. **Get your URL**:
   - Click on your deployment
   - Go to "Settings" → "Domains"
   - Click "Generate Domain"
   - Your app will be available at: `https://your-app.up.railway.app`

### Method 2: Deploy with Railway CLI

1. **Install Railway CLI**:
```bash
npm install -g @railway/cli
# or
brew install railway
```

2. **Login**:
```bash
railway login
```

3. **Initialize and Deploy**:
```bash
cd /Volumes/Data/Work/Demo-MCP

# Link to Railway (creates new project)
railway init

# Deploy
railway up

# Get the URL
railway domain
```

4. **Open your app**:
```bash
railway open
```

## Configuration

### Environment Variables (Optional)

If you need to add environment variables:

```bash
# Using CLI
railway variables set KEY=VALUE

# Or in Railway Dashboard
# Project → Variables → Add Variable
```

For production, you might want:
```bash
railway variables set ENVIRONMENT=production
railway variables set LOG_LEVEL=info
```

## Testing Your Deployment

Once deployed, test your endpoints:

```bash
# Replace with your Railway URL
RAILWAY_URL="https://your-app.up.railway.app"

# Test health check
curl $RAILWAY_URL/

# Test search accounts (with mock token)
curl -H "Authorization: mock-token" "$RAILWAY_URL/search_accounts?q=acme"

# Test get account details
curl -H "Authorization: mock-token" "$RAILWAY_URL/get_account_details/1"
```

## Files Configured for Railway

✅ **app.py** - Fixed syntax error, clean FastAPI app
✅ **Procfile** - Uses `$PORT` environment variable (Railway provides this)
✅ **railway.json** - Railway-specific configuration
✅ **requirements.txt** - All dependencies with versions

## Key Differences from AWS EB

| Feature | AWS EB | Railway |
|---------|--------|---------|
| Port Configuration | Fixed (8000) | Dynamic (`$PORT`) |
| Application Variable | Needs `application = app` | Uses `app` directly |
| Configuration | `.ebextensions/` | `railway.json` |
| Deployment Time | 5-10 minutes | 1-2 minutes |
| Free Tier | Limited | $5 free credit/month |

## Monitoring & Logs

### View Logs:
```bash
# CLI
railway logs

# Or in Dashboard
# Project → Deployments → View Logs
```

### Metrics:
- Go to Railway Dashboard
- Click on your service
- View CPU, Memory, and Network usage

## Custom Domain (Optional)

1. Go to Railway Dashboard → Settings → Domains
2. Click "Custom Domain"
3. Add your domain (e.g., `api.yourdomain.com`)
4. Update your DNS with the provided CNAME record

## Pricing

- **Free**: $5 credit/month (good for small apps)
- **Developer**: $5/month + usage
- No credit card required for free tier

## Troubleshooting

### Issue: Build Failed
**Check**: 
- View build logs in Railway dashboard
- Ensure `requirements.txt` has all dependencies
- Check Python version compatibility

### Issue: App Not Starting
**Check**:
```bash
# Test locally first
uvicorn app:app --host 0.0.0.0 --port 8000

# Check Railway logs
railway logs
```

### Issue: Import Errors
**Solution**: Make sure all files are committed and pushed:
```bash
git status
git add .
git commit -m "Add missing files"
git push
railway up
```

## Updating Your App

```bash
# Make changes
git add .
git commit -m "Your changes"
git push

# Railway auto-deploys on push!
# Or manually trigger:
railway up
```

## Cleanup

To delete your Railway project:
- Go to Railway Dashboard
- Project Settings → Danger Zone → Delete Project

## Advantages of Railway

✅ **Automatic HTTPS** - SSL certificates included
✅ **Fast deployments** - Usually under 2 minutes
✅ **Auto-deployments** - Pushes to main branch auto-deploy
✅ **Simple pricing** - Pay for what you use
✅ **Great for APIs** - Perfect for FastAPI/Flask/Django
✅ **Built-in monitoring** - Logs, metrics, and alerts

## Support

- [Railway Docs](https://docs.railway.app)
- [Railway Discord](https://discord.gg/railway)
- [Railway Status](https://status.railway.app)

---

## Quick Commands Cheat Sheet

```bash
# Login
railway login

# Initialize project
railway init

# Deploy
railway up

# View logs
railway logs

# Open dashboard
railway open

# Generate public URL
railway domain

# Set environment variable
railway variables set KEY=VALUE

# Link to existing project
railway link
```

