import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vite.dev/config/
export default defineConfig({
  plugins: [svelte()],
  build: {
    rollupOptions: {
      input: {
        'book_detail': './src/book_detail.js',
      },
      output: {
        entryFileNames: '../static/[name]-[hash].js',
        chunkFileNames: '../static/[name]-[hash].js',
        assetFileNames: '../static/[name].[ext]'
      }
    }
  },
  server: {
    host: true,
    port: 5173
  }
})
