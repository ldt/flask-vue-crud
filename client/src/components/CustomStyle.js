import { Mark } from "tiptap";
// import { Mark, TextSelection } from "tiptap";
import { updateMark } from "tiptap-commands";
// import { getMarkRange } from "tiptap-utils";

import _ from "lodash";

/* eslint class-methods-use-this: ["error", { "exceptMethods": ["name", "defaultOptions", "schema", "commands"] }] */

export default class CustomStyle extends Mark {
  constructor(entities) {
    super();
    this.entities = _.keyBy(entities, "levelName");
    this.levels = _.keys(this.entities);
  }

  get name() {
    return "customstyle";
  }

  get defaultOptions() {
    return {
      levels: this.levels
    };
  }

  get schema() {
    return {
      attrs: {
        level: {
          default: this.levels[0]
        }
      },
      parseDOM: [
        {
          tag: "span.custom-style",
          getAttrs(dom) {
            return { level: dom.classList[1] };
          }
        }
      ],
      toDOM: mark => {
        return ["span", { class: `custom-style ${mark.attrs.level}` }, 0];
      }
    };
  }

  commands({ type }) {
    return attrs => updateMark(type, attrs);
  }
}
