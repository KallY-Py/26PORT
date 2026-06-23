const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  publicPath: process.env.NODE_ENV === 'production' 
    ? '/Port26/' 
    : '/',
  outputDir: 'docs', 
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