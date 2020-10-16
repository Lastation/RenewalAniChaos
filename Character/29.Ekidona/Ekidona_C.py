import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] < 16)
         {
            RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            f.DotShape(cp, 1, "40 + 1n Mojo", 0, 0);
            f.DotShape(cp, 1, "60 + 1n Archon", 0, 0);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            Order("40 + 1n Mojo", cp, "Anywhere", Attack, "Anywhere");
         }

         var x = 0;
         var y = 0;

         if (f.loop[cp] == 8) { x = 0; y = -50; }
         if (f.loop[cp] == 9) { x = -100; y = 100; }
         if (f.loop[cp] == 10) { x = 0; y = 50; }
         if (f.loop[cp] == 11) { x = 100; y = -100; }
         if (f.loop[cp] == 12) { x = -50; y = 0; }
         if (f.loop[cp] == 13) { x = 100; y = 100; }
         if (f.loop[cp] == 14) { x = 50; y = 0; }
         if (f.loop[cp] == 15) { x = -100; y = -100; }

         if (f.loop[cp] >= 8)
         {
            f.DotShape(cp, 9, "60 + 1n High Templar", x, y);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 16)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {
            RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
            f.SquareShape(cp, 1, "60 + 1n High Templar", 50, 0);
            f.SquareShape(cp, 1, "60 + 1n High Templar", 100, 100);
            f.SquareShape(cp, 8, " Unit. Schnee", 50, 0);
            f.SquareShape(cp, 8, " Unit. Schnee", 100, 100);
            KillUnitAt(All, " Unit. Schnee", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "60 + 1n High Templar", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("60 + 1n High Templar", cp, "Anywhere", Attack, f.location[cp]);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 4)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

         f.SkillEnd(cp);
      }
   }
}