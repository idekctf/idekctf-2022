async (url, ctx) => {
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
}
