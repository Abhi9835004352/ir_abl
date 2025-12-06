# 🚀 Deployment Guide

## Production Deployment Options

This guide covers deploying your Intelligent Search Engine to production.

---

## 1. Docker Compose (Recommended for Local/Single Server)

### Prerequisites
- Docker & Docker Compose installed
- SerpAPI key

### Setup

1. **Create .env file**
   ```bash
   cat > .env << EOF
   SERPAPI_KEY=your_serpapi_key_here
   EOF
   ```

2. **Start services**
   ```bash
   docker-compose up -d
   ```

3. **Verify**
   ```bash
   curl http://localhost:8000/health
   curl http://localhost:5173
   ```

4. **View logs**
   ```bash
   docker-compose logs -f
   ```

5. **Stop services**
   ```bash
   docker-compose down
   ```

### Database Backup
```bash
# Backup MongoDB
docker-compose exec mongodb mongodump --out /data/backup

# Restore MongoDB
docker-compose exec mongodb mongorestore /data/backup
```

---

## 2. Heroku Deployment

### Backend on Heroku

1. **Install Heroku CLI**
   ```bash
   brew tap heroku/brew && brew install heroku
   heroku login
   ```

2. **Create Heroku app**
   ```bash
   heroku create your-app-name
   ```

3. **Add MongoDB Atlas**
   ```bash
   # Go to https://www.mongodb.com/cloud/atlas
   # Create free tier cluster
   # Get connection string
   heroku config:set MONGO_URI="mongodb+srv://user:pass@cluster.mongodb.net/db"
   ```

4. **Add SerpAPI key**
   ```bash
   heroku config:set SERPAPI_KEY="your_key_here"
   ```

5. **Create Procfile** (backend/)
   ```
   web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```

6. **Deploy**
   ```bash
   git push heroku main
   ```

7. **View logs**
   ```bash
   heroku logs --tail
   ```

### Frontend on Vercel

1. **Install Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Deploy**
   ```bash
   cd frontend
   vercel
   ```

3. **Set environment variable**
   - Go to Vercel dashboard
   - Settings → Environment Variables
   - Add: `VITE_API_URL=https://your-heroku-app.herokuapp.com`

4. **Configure vite.config.js**
   ```javascript
   import { defineConfig } from 'vite'
   import react from '@vitejs/plugin-react'

   export default defineConfig({
     plugins: [react()],
     define: {
       'process.env.VITE_API_URL': JSON.stringify(process.env.VITE_API_URL)
     }
   })
   ```

---

## 3. AWS Deployment

### Option A: ECS + RDS + CloudFront

1. **Create ECR repository**
   ```bash
   aws ecr create-repository --repository-name search-engine-backend
   aws ecr create-repository --repository-name search-engine-frontend
   ```

2. **Build and push images**
   ```bash
   # Backend
   docker build -t search-engine-backend backend/
   docker tag search-engine-backend:latest [account].dkr.ecr.[region].amazonaws.com/search-engine-backend:latest
   docker push [account].dkr.ecr.[region].amazonaws.com/search-engine-backend:latest
   ```

3. **Create RDS MongoDB** (or use MongoDB Atlas)

4. **Create ECS cluster and services**

5. **Set up CloudFront** for frontend

### Option B: Elastic Beanstalk

1. **Install EB CLI**
   ```bash
   pip install awsebcli
   ```

2. **Initialize**
   ```bash
   eb init -p python-3.11 search-engine
   ```

3. **Create environment**
   ```bash
   eb create production
   ```

4. **Deploy**
   ```bash
   eb deploy
   ```

---

## 4. Google Cloud Platform

### App Engine Deployment

1. **Create app.yaml** (backend/)
   ```yaml
   runtime: python39
   env: standard

   handlers:
   - url: /.*
     script: auto
     secure: always

   env_variables:
     MONGO_URI: "mongodb+srv://user:pass@cluster.mongodb.net/db"
     SERPAPI_KEY: "your_key"
   ```

2. **Deploy**
   ```bash
   gcloud app deploy backend/app.yaml
   ```

### Cloud Run Deployment

1. **Build image**
   ```bash
   gcloud builds submit --tag gcr.io/[project]/search-engine-backend backend/
   ```

2. **Deploy**
   ```bash
   gcloud run deploy search-engine-backend \
     --image gcr.io/[project]/search-engine-backend \
     --platform managed \
     --region us-central1 \
     --set-env-vars MONGO_URI="...",SERPAPI_KEY="..."
   ```

---

## 5. DigitalOcean

### App Platform

1. **Connect repository** (GitHub/GitLab)

2. **Create app spec** (app.yaml)
   ```yaml
   name: search-engine
   services:
   - name: backend
     github:
       repo: your-repo/ir_abl
       branch: main
     build_command: pip install -r backend/requirements.txt
     run_command: uvicorn app.main:app --host 0.0.0.0 --port 8080
     http_port: 8080
     envs:
     - key: MONGO_URI
       value: ${db.connection.postgresql_uri}
       
   - name: frontend
     github:
       repo: your-repo/ir_abl
       branch: main
     build_command: cd frontend && npm install && npm run build
     run_command: npm run preview
     http_port: 5173

   databases:
   - name: db
     engine: MONGODB
     version: "5"
   ```

3. **Deploy**
   ```bash
   doctl apps create --spec app.yaml
   ```

---

## 6. Production Best Practices

### Security

1. **Environment Variables**
   - Never commit .env files
   - Use secrets management (AWS Secrets Manager, HashiCorp Vault)
   - Rotate API keys regularly

2. **Database**
   - Enable MongoDB authentication
   - Use strong passwords
   - Enable TLS/SSL connections
   - Regular backups

3. **API**
   - Add rate limiting
   - Implement authentication if needed
   - Use HTTPS everywhere
   - Add CORS restrictions

4. **Frontend**
   - Use HTTPS
   - Set Security headers
   - Implement CSP (Content Security Policy)
   - Regular security audits

### Performance

1. **Caching**
   - Use Redis for search query caching
   - Cache frequently accessed URLs
   - CloudFlare CDN for static files

2. **Database Optimization**
   - Create appropriate indexes
   - Monitor query performance
   - Regular database maintenance

3. **API Optimization**
   - Implement pagination
   - Rate limiting
   - Gzip compression
   - Response caching

### Monitoring

1. **Backend Monitoring**
   - Sentry for error tracking
   - New Relic or DataDog for APM
   - CloudWatch for logs

2. **Frontend Monitoring**
   - Sentry for JavaScript errors
   - Google Analytics for usage
   - Lighthouse for performance

3. **Database Monitoring**
   - MongoDB Atlas monitoring
   - Query performance analysis
   - Storage usage tracking

### Scaling

1. **Horizontal Scaling**
   - Load balancer (ALB, NGINX)
   - Multiple backend instances
   - Database replication

2. **Vertical Scaling**
   - Increase server resources
   - Optimize code
   - Better caching strategy

---

## 7. CI/CD Pipeline

### GitHub Actions Example

**`.github/workflows/deploy.yml`**
```yaml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.11'
      - run: pip install -r backend/requirements.txt
      - run: pytest backend/tests/

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to production
        run: |
          # Your deployment commands here
```

---

## 8. Domain & SSL

### Let's Encrypt (Free SSL)

1. **Using Certbot**
   ```bash
   certbot certonly --standalone -d yourdomain.com
   ```

2. **Auto-renewal**
   ```bash
   sudo systemctl enable certbot.timer
   sudo systemctl start certbot.timer
   ```

### Custom Domain

1. **Update DNS records**
   ```
   A record: yourdomain.com → your-server-ip
   CNAME: www.yourdomain.com → yourdomain.com
   ```

2. **Configure reverse proxy**
   - Use NGINX or Apache
   - Enable SSL certificates
   - Redirect HTTP to HTTPS

---

## 9. Troubleshooting Production Issues

### Database Connection Issues
```bash
# Check MongoDB connection
mongosh "mongodb://user:pass@host:27017/db"

# Check environment variables
env | grep MONGO
```

### API Not Responding
```bash
# Check service status
systemctl status search-engine-backend

# View logs
journalctl -u search-engine-backend -f

# Test endpoint
curl -v http://localhost:8000/health
```

### Frontend Not Loading
```bash
# Check build
npm run build --prefix frontend

# Test server
cd frontend && npm run preview
```

---

## 10. Backup & Recovery

### Database Backup

```bash
# Full backup
mongodump --uri "mongodb://user:pass@host/db" --out ./backup

# Incremental backup (requires journaling)
mongodump --uri "mongodb://user:pass@host/db" --out ./backup

# Restore
mongorestore ./backup --uri "mongodb://user:pass@host/db"
```

### Application Backup

```bash
# Backup entire application
tar -czf search-engine-backup.tar.gz /path/to/app

# Restore
tar -xzf search-engine-backup.tar.gz
```

---

## 11. Cost Optimization

### Free/Low-Cost Options

- **Frontend**: Vercel (free tier, $20/month pro)
- **Backend**: Heroku (deprecated - use Railway: $5/month)
- **Database**: MongoDB Atlas (free tier, $57/month production)
- **Domain**: Namecheap ($1 first year)
- **SSL**: Let's Encrypt (free)

### Expected Costs

| Component | Low Traffic | High Traffic |
|-----------|------------|-------------|
| Backend | $0-10/mo | $50-500/mo |
| Frontend | $0-5/mo | $20-100/mo |
| Database | $57/mo | $200-1000/mo |
| Domain | $10/mo | $10/mo |
| **Total** | **$67-82/mo** | **$280-1610/mo** |

---

## 12. Maintenance Checklist

- [ ] Daily: Monitor error logs
- [ ] Weekly: Check database size
- [ ] Monthly: Update dependencies
- [ ] Quarterly: Security audit
- [ ] Annually: Full system review

---

## Support

For deployment questions:
- Check cloud provider documentation
- Review application logs
- Test locally first
- Contact cloud provider support

Good luck with your deployment! 🚀
