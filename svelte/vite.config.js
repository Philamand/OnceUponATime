import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import tailwindcss from '@tailwindcss/vite'
import { resolve } from 'node:path'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    svelte(),
    tailwindcss(),
  ],
  build: {
    outDir: resolve(__dirname, '../static/'),
    emptyOutDir: false,
    rollupOptions: {
      input: {
        'book_detail': './src/book_detail.js',
        'documentary_list': './src/documentary_list.js',
        'htmx': './src/htmx.js',
        'dock': './src/dock.js',
        'swiper': './src/swiper.js',
        'styles': './src/style.css'
      },
      output: {
        entryFileNames: 'svelte/[name].js',
        chunkFileNames: 'svelte/[name]-[hash].js',
        assetFileNames: '[name].[ext]'
      }
    }
  },
  server: {
    host: true,
    port: 5173
  }
})
