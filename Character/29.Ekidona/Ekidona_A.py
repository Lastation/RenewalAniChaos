import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         var x = 0;
         var y = 0;

         if (f.loop[cp] == 0) { x = 100; y = 100; }
         if (f.loop[cp] == 2) { x = -100; y = 100; }
         if (f.loop[cp] == 4) { x = -100; y = -100; }
         if (f.loop[cp] == 6) { x = 100; y = -100; }

         f.SquareShapeAt(cp, 1, "40 + 1n Gantrithor", 50, 50, x, y);
         f.SquareShapeAt(cp, 1, "60 + 1n Dragoon", 50, 50, x, y);
         KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 8)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {
            f.SquareShape(cp, 1, "40 + 1n Mojo", 100, 0);
            f.SquareShape(cp, 1, "60 + 1n Archon", 100, 0);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
         }
         if (f.loop[cp] == 2)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Mojo", 100, 100);
            f.SquareShape(cp, 1, "60 + 1n Archon", 100, 100);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
         }
         if (f.loop[cp] == 4)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
         }
         if (f.loop[cp] == 6)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            f.SquareShape(cp, 1, "60 + 1n Danimoth", 50, 50);
            f.SquareShape(cp, 1, "60 + 1n Danimoth", 50, 0);
            f.SquareShape(cp, 1, "60 + 1n Archon", 50, 50);
            f.SquareShape(cp, 1, "60 + 1n Archon", 50, 0);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("60 + 1n Danimoth", cp, "Anywhere", Attack, f.location[cp]);
         }


         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 8)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);
         KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", cp);

         f.SkillEnd(cp);
      }
   }
}