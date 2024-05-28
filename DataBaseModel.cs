using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DocumentsArchive
{
    public class BookshelfMain
    {
        public int Id { get; set; }
        public string Stand { get; set; }
        public string Shelf { get; set; }
        public string MainItemName { get; set; }
        public List<BookshelfSub> SubItems { get; set; }
    }

    public class BookshelfSub
    {
        public int Id { get; set; }
        public string SubItemName { get; set; }
        public bool IsTaken { get; set; }
        public string LoginName { get; set; }
        public int BookshelfMainId { get; set; }
    }
}
