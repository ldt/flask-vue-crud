import { Mark } from "tiptap";
// import { Mark, TextSelection } from "tiptap";
import { updateMark } from "tiptap-commands";
// import { getMarkRange } from "tiptap-utils";

/* eslint class-methods-use-this: ["error", { "exceptMethods": ["name", "defaultOptions", "schema", "commands"] }] */

export default class CustomStyle extends Mark {
  get name() {
    return "customstyle";
  }

  get defaultOptions() {
    return {
      levels: ["action", "tool", "part"]
    };
  }

  get schema() {
    return {
      attrs: {
        level: {
          default: "action"
        }
      },
      parseDOM: [
        {
          tag: "span.custom-style",
          getAttrs(dom) {
            // console.log(dom.classList[1]);
            return { level: dom.classList[1] };
          }
        }
      ],
      toDOM: mark => {
        return ["span", { class: `custom-style ner-${mark.attrs.level}` }, 0];
      }
    };
  }

  commands({ type }) {
    return attrs => updateMark(type, attrs);
  }
}
