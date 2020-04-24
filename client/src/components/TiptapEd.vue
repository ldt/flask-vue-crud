<template>
  <div class="editor">
    <editor-menu-bubble
      :editor="editor"
      :keep-in-bounds="keepInBounds"
      v-slot="{ commands, isActive, menu }"
    >
      <div
        class="menububble"
        :class="{ 'is-active': menu.isActive }"
        :style="`left: ${menu.left}px; bottom: ${menu.bottom}px;`"
      >
        <button
          v-for="e in entities"
          :key="e.levelName"
          class="menububble__button"
          :class="{ 'is-active': isActive.customstyle({ level: e.levelName }) }"
          @click="commands.customstyle({ level: e.cssName })"
        >
          {{ e.tooltipName }}
        </button>
      </div>
    </editor-menu-bubble>

    <editor-content class="editor__content" :editor="editor" />
  </div>
</template>

<script>
import { mapGetters } from "vuex";

import { Editor, EditorContent, EditorMenuBubble } from "tiptap";
import {
  Blockquote,
  BulletList,
  CodeBlock,
  HardBreak,
  Heading,
  ListItem,
  OrderedList,
  TodoItem,
  TodoList,
  Bold,
  Code,
  Italic,
  Link,
  Strike,
  Underline,
  History
} from "tiptap-extensions";
import CustomStyle from "./CustomStyle";

export default {
  components: {
    EditorContent,
    EditorMenuBubble
  },
  data() {
    return {
      keepInBounds: true,
      editor: this.createEditor(),
      entities: []
    };
  },
  computed: {
    ...mapGetters(["currentEntities", "currentProject"])
  },
  methods: {
    updateEntityList() {
      // fill this.entities by parsing this.currentEntities
      this.entities = [];
      let i = 0;
      this.currentEntities.forEach(element => {
        this.entities.push({
          tooltipName: element.name.toUpperCase(),
          cssName: `ner-${i}`,
          levelName: element.name.toLowerCase()
        });
        i += 1;
      });
    },
    handleMouseUp(view) {
      const from = view.state.selection.$anchor.pos;
      const to = view.state.selection.$head.pos;
      const { doc } = view.state;
      const $start = doc.resolve(from);

      const nodeContent = $start.parent.textContent;
      const nodeTextStart = nodeContent.substring(0, $start.parentOffset);
      const indexStart =
        this.findClosestSeparatorBefore($start.parentOffset, nodeTextStart) +
        $start.pos -
        $start.parentOffset;
      const $end = doc.resolve(to);
      const nodeTextEnd = nodeContent.substring($end.parentOffset);
      const indexStop = this.findClosestSeparatorAfter(to, nodeTextEnd) + $end.pos;
      this.editor.setSelection(indexStart, indexStop);
    },
    findClosestSeparatorBefore(index, text) {
      const separatorsIndices = [];
      [...text].forEach((char, i) => {
        if (char.match(/\W+/)) separatorsIndices.push(i);
      });
      if (!separatorsIndices || separatorsIndices.length === 0) return 0;

      // if index < separatorsIndices[0] then return 1 (start of the text)
      if (index <= separatorsIndices[0]) return 1;
      const closest = separatorsIndices.reduce((prev, curr) => {
        if (index - curr < 0) return prev;
        return curr;
      });
      return closest + 1;
    },
    findClosestSeparatorAfter(index, text) {
      const separatorsIndices = [];
      [...text].forEach((char, i) => {
        if (char.match(/\W+/)) separatorsIndices.push(i);
      });
      if (!separatorsIndices || separatorsIndices.length === 0) return text.length;
      return separatorsIndices[0];
    },
    createEditor() {
      const edProps = {
        handleDOMEvents: {
          mouseup: this.handleMouseUp
        }
      };

      // eslint-disable-next-line
      return new Editor({
        editorProps: edProps,
        extensions: [
          new Blockquote(),
          new BulletList(),
          new CodeBlock(),
          new HardBreak(),
          new Heading({ levels: [1, 2, 3] }),
          new ListItem(),
          new OrderedList(),
          new TodoItem(),
          new TodoList(),
          new Link(),
          new Bold(),
          new Code(),
          new Italic(),
          new Strike(),
          new Underline(),
          new History(),
          new CustomStyle(this.entities)
        ],
        content: `
<h1>Remove synchronization rope</h1>
<p>The topic describes the procedures to remove synchronization rope.</p>
<p>
<ol>
  <li>Remove the door closing spring off the door panel.</li>
  <li>Remove the bolts which fix the synchronization rope using hex key (4mm).</li>
  <li>Remove the holding bracket of synchronization rope using hex key (4mm).
    a.  Remove the screws.
    b.  Move the holding bracket outwards.
  </li>
4.  Remove the synchronization rope using the spanner (8mm).
</ul>
Related tasks

-   Take elevator out of service
-   Prepare before replacement
</p>
        `
      });
    }
  },
  beforeDestroy() {
    this.editor.destroy();
  },
  mounted() {
    this.updateEntityList();

    // this.$store.subscribe(mutation => {
    //   console.log("mutation.type", mutation.type);
    //   console.log("mutation.payload", mutation.payload);
    // });
    this.$store.subscribe(mutation => {
      if (mutation.type === "SET_CURRENT_PROJECT") {
        this.updateEntityList();
      }
    });
  }
};
</script>
<style lang="scss" src="./style.scss">
.editor {
  border: 1px solid blue;
}
</style>
