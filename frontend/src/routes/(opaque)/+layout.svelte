<script lang="ts">
    import { transparent } from '../../stores';
      import type { LayoutData } from './$types';
      
      export let data: LayoutData;
  
      $transparent = true
  </script>
  <slot></slot>