const sleep = time => new Promise(resolve => setTimeout(resolve, time))

const challenges = new Map([
  ['stargazer', {
    name: 'Stargazer',
    timeout: 100000,
    handler: async (url, ctx) => {
      // We only allow visiting backend.magic.world
      if (new URL(url).hostname !== 'backend.magic.world') {
        return;
      }

      const page = await ctx.newPage()
      try {
          await page.goto('http://backend.magic.world:1337', { timeout: 2 * 1000, waitUntil: 'networkidle2' })
          await page.waitForNetworkIdle({idleTime: 1000, timeout: 2*1000})
          await page.setCookie({'name': "FLAG", "value": 'idek{G4z1n9_Th3_5T4R_Ch4s1ng_Th3_m00n}', "domain":".backend.magic.world"})

          await page.goto(url, { timeout: 2 * 1000, waitUntil: 'networkidle2' })
          await page.waitForNetworkIdle({idleTime: 20 * 1000})

      } catch (err){
          console.log(err);
      } finally {
          await page.close()
          await ctx.close()
      }

      console.log(`Done visiting -> ${url}`)
    }
  }],
  ['badblocker', {
    name: 'BadBlocker',
    timeout: 15000,
    handler: async (url, ctx) => {
      let page = await ctx.newPage();
  
      await page.goto("http://badblocker.chal.idek.team:1337", {
          waitUntil: "domcontentloaded"
      });
  
      await page.evaluate(flag => {
          window.localStorage.setItem("initialised", true);
          window.localStorage.setItem("blockHistory", JSON.stringify({
              "1592953200000": {
                  "url": flag,
                  "numBlocked": 9876734123
              }
          }));
      }, "idek{maybe_the_real_ads_were_the_bads_we_blocked_along_the_way_3e034c37ec0275ea}");
  
      await page.goto(url, {
          waitUntil: "domcontentloaded"
      });
  
      await page.waitForTimeout(10000);
    },
  }],
  ['jsonbeautifier', {
    name: 'Json Beautifier',
    timeout: 10000,
    handler: async (url, ctx) => {
        let page = await ctx.newPage();
        
        await page.setCookie({
                "value": "idek{w0w_th4t_JS0N_i5_v3ry_beautiful!!!}",
                "domain": "json-beautifier.chal.idek.team",
                "name": "flag",
        });

        await page.goto(url, {
                waitUntil: "domcontentloaded"
        });

        await page.waitForTimeout(3000);
    },
  }]
])

module.exports = {
  challenges
}

