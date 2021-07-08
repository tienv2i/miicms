const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    entry: {
        app: './frontend/index.js',
    },
    output: {
        path: path.resolve(__dirname, '../frontend/dist'),
        publicPath: '/static/',
        filename: 'js/[name].js'
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /(node_modules|bower_components)/,
                loader: 'babel-loader'
            },
            {
                test: /\.(sa|sc|c)ss$/,
                use: [
                  MiniCssExtractPlugin.loader,
                  "css-loader",
                  "postcss-loader",
                  "sass-loader",
                ],
            },
            {
                test: /\.(png|jpe?g|gif|svg)$/i,
                use: [
                  {
                    loader: 'file-loader',
                    options: {
                        filename: 'images/[name].[hash:8].[ext]'
                    }
                  },
                ],
            },
            {
                test: /\.(woff|ttf|oet)$/i,
                use: [
                  {
                    loader: 'file-loader',
                    options: {
                        filename: 'fonts/[name].[hash:8].[ext]'
                    }
                  },
                ],
            }
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
            filename: 'index.html'
        }),
        new MiniCssExtractPlugin({
            filename: 'css/style.css',
        }),
        new CleanWebpackPlugin(),
        new BundleTracker({
            filename: './frontend/webpack-stats.json'
        })
    ],
    optimization: {
        splitChunks: {
          chunks: "all"
        }
    }
}