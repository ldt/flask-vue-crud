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
          class="menububble__button"
          :class="{ 'is-active': isActive.customstyle({ level: 'action' }) }"
          @click="commands.customstyle({ level: 'action' })"
        >
          Action
        </button>
        <button
          class="menububble__button"
          :class="{ 'is-active': isActive.customstyle({ level: 'tool' }) }"
          @click="commands.customstyle({ level: 'tool' })"
        >
          Tool
        </button>
        <button
          class="menububble__button"
          :class="{ 'is-active': isActive.customstyle({ level: 'part' }) }"
          @click="commands.customstyle({ level: 'part' })"
        >
          Part
        </button>
      </div>
    </editor-menu-bubble>

    <editor-content class="editor__content" :editor="editor" />
  </div>
</template>

<script>
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
      editor: this.createEditor()
    };
  },
  beforeDestroy() {
    this.editor.destroy();
  },
  methods: {
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
          new CustomStyle()
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
  }
};
</script>
<style lang="scss" src="./style.scss">
.editor {
  border: 1px solid blue;
}
</style>
