const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  publicPath: process.env.NODE_ENV === 'production' 
    ? '/PORTFOl/'  // Replace with your repository name
    : '/',
  outputDir: 'docs',  // Output to docs folder instead of dist
  assetsDir: 'assets',
  indexPath: 'index.html',
  filenameHashing: true,
  pages: {
    index: {
      entry: 'src/main.js',
      template: 'public/index.html',
      filename: 'index.html',
      title: 'JC Porcopio - Portfolio'
    }
  }
})