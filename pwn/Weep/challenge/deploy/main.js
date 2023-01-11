import puppeteer from 'puppeteer'
import express from 'express'
import rateLimit from 'express-rate-limit'

const app = express()
app.use(express.static('static'))
app.use(express.json())

const port = 1337
let browser

async function visit (url) {
  const ctx = await browser.createIncognitoBrowserContext()
  const page = await ctx.newPage()

  await page.setCookie({
    name: 'flag',
    value: "idek{Now_When_will_we_get_security_checks_in_the_heap_allocator?}",
    domain: 'localhost',
    sameSite: 'strict',
    httpOnly: false
  })

  try {
    await page.goto(url, { timeout: 3000, waitUntil: 'networkidle2' })
    await page.waitForTimeout(3000)
  } finally {
    await page.close()
    await ctx.close()
  }
}

app.use(
  '/visit',
  rateLimit({
    windowMs: 60 * 1000,
    max: 5,
    message: { error: 'Too many requests, try again later' }
  })
)

app.post('/visit', async (req, res) => {
  var url = req.body.url
  if (
    url === undefined
  ) {
    return res.status(400).send({ error: 'Empty Body' })
  }
  url = 'http://localhost:1337/#'+url

  try {
    console.log(`[*] Visiting ${url}`)
    await visit(url)
    console.log(`[*] Done visiting ${url}`)
    return res.sendStatus(200)
  } catch (e) {
    console.error(`[-] Error visiting ${url}: ${e.message}`)
    return res.status(400).send({ error: e.message })
  }
})

app.listen(port, async () => {
  browser = await puppeteer.launch({
    pipe: true,
    dumpio: true,
    args: [
    //  '--disable-dev-shm-usage', // Docker stuff
    //  '--js-flags=--jitless' // No Chrome n-days please
    ]
  })
  console.log(`[*] Listening on port ${port} ...`)
})