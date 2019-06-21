const BundleTracker = require("webpack-bundle-tracker");

const bundlePath =
  process.env.NODE_ENV === "production"
    ? "../frontend/webpack-stats-prod.json"
    : "../frontend/webpack-stats.json";

const publicPath =
  process.env.NODE_ENV === "production" ? "/" : "http://127.0.0.1:8080/";

module.exports = {
  publicPath: publicPath,
  outputDir: "./dist/",

  chainWebpack: config => {
    config.optimization.splitChunks(false);

    config
      .plugin("BundleTracker")
      .use(BundleTracker, [{ filename: bundlePath }]);

    config.resolve.alias.set("__STATIC__", "static");

    config.devServer
      .public("http://0.0.0.0:8080")
      .host("0.0.0.0")
      .port(8080)
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .headers({ "Access-Control-Allow-Origin": ["*"] });
  }
};
