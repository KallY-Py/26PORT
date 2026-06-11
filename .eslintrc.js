module.exports = {
  root: true,
  env: {
    node: true,
    browser: true,
    es2021: true
  },
  extends: [
    'plugin:vue/vue3-essential',
    'eslint:recommended'
  ],
  parserOptions: {
    parser: '@babel/eslint-parser',
    ecmaVersion: 2021,
    sourceType: 'module'
  },
  rules: {
    // Allow debugger statements (for anti-debugging protection)
    'no-debugger': 'off',
    
    // Allow console statements (for development)
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    
    // Disable unused variable warnings for template refs
    'no-unused-vars': 'warn',
    
    // Allow empty functions (for protection methods)
    'no-empty': 'warn',
    
    // Disable alert usage warnings
    'no-alert': 'off',
    
    // Allow underscore dangle (for internal variables)
    'no-underscore-dangle': 'off',
    
    // Allow modifying function parameters (for event handlers)
    'no-param-reassign': 'off',
    
    // Disable camelcase for API responses
    'camelcase': 'off',
    
    // Allow mixed operators
    'no-mixed-operators': 'off',
    
    // Allow spaces inside parentheses
    'space-in-parens': 'off',
    
    // Disable implicit arrow linebreak
    'implicit-arrow-linebreak': 'off',
    
    // Disable function-paren-newline
    'function-paren-newline': 'off',
    
    // Disable operator-linebreak
    'operator-linebreak': 'off',
    
    // Allow longer lines
    'max-len': ['warn', { code: 200 }],
    
    // Disable arrow body style requirement
    'arrow-body-style': 'off',
    
    // Allow no-plusplus
    'no-plusplus': 'off',
    
    // Disable requirement for default exports
    'import/prefer-default-export': 'off',
    
    // Allow continue statements
    'no-continue': 'off',
    
    // Allow rest spread syntax
    'prefer-rest-params': 'off',
    
    // Disable vue rules that might interfere
    'vue/multi-word-component-names': 'off',
    'vue/no-v-model-argument': 'off',
    'vue/require-default-prop': 'off',
    'vue/require-prop-types': 'off',
    'vue/singleline-html-element-content-newline': 'off',
    'vue/max-attributes-per-line': 'off',
    'vue/html-indent': 'off',
    'vue/script-indent': 'off',
    'vue/html-closing-bracket-newline': 'off',
    'vue/first-attribute-linebreak': 'off',
    'vue/attributes-order': 'off'
  },
  globals: {
    // Define global variables used in your project
    'defineProps': 'readonly',
    'defineEmits': 'readonly',
    'defineExpose': 'readonly',
    'withDefaults': 'readonly'
  },
  overrides: [
    {
      files: ['*.vue'],
      rules: {
        // Specific rules for Vue files
        'no-debugger': 'off',
        'no-console': 'off'
      }
    }
  ],
  ignorePatterns: [
    'node_modules/',
    'dist/',
    'build/',
    '*.config.js',
    '!.eslintrc.js'
  ]
}