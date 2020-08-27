'use strict'

const { VueLoaderPlugin } = require('vue-loader');
const webpack = require('webpack');
const path    = require('path');


module.exports = {
  // runtimeCompiler: true,
  entry: [

    path.join(__dirname, 'resources/js', 'app.js'),
  ],
  module: {
    rules: [
      {
        test: /\.vue$/,
        use: 'vue-loader'
      },
      {
        test:/\.css$/,
        use:['vue-style-loader', 'css-loader' ]
      },
      {
        test:/\.scss$/,
        use:[
          'vue-style-loader',
          "css-loader",          
        ]
      }
    ]
  },
  resolve: {
    modules: ["node_modules"],
    extensions: [ '.js', '.vue' , '.json', '*'],
    alias: {
      'vue$': 'vue/dist/vue.esm.js',
      '@': path.resolve(__dirname, 'resources/js/'),
      '@components': path.resolve(__dirname, 'resources/js/components'),
    }
  },
  output: {

    filename: 'app.js',
    path: path.resolve(__dirname, 'public/static/js'),
    publicPath: 'static/js',
  }, 
  devServer: {

    contentBase: path.resolve(__dirname, 'public' ),
  },
  plugins: [

    new VueLoaderPlugin(),
  ]
}