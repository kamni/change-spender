var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    context: __dirname,
    resolve: {
        extensions: ['', '.js', '.jsx']
    },
    entry: './calculator/static/js/main',
    output: {
        path: path.resolve('./static/bundles/'),
        filename: "[name]-[hash].js"
    },
    module: {
        loaders: [{
            test: /\.(js|jsx)$/,
            exclude: /node_modules/,
            loader: "babel",
            query: { presets:['react'] }
        }]
    },
    plugins: [
        new BundleTracker({filename: './webpack-stats.json'})
    ]
};