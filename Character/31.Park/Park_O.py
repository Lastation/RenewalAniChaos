import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] < 12)
         {
            f.SquareShape(cp, 1, "Bengalaas (Jungle)", 32, 32);
            KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", cp);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 12)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 12 )
         {
            f.SquareShape(cp, 1, "Bengalaas (Jungle)", 64, 64);
            f.SquareShape(cp, 1, "Protoss Dark Archon", 64, 0);
            KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
         }

       f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 12)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }

      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] == 8 )
         {
            f.NxNSquareShape(cp, 1, "50 + 1n Battlecruiser", 3, 100);
            f.NxNSquareShape(cp, 1, "Protoss Dark Archon", 3, 50);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
         }
       f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 10)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }

      else if (f.count[cp] == 3)
      {
         SetDeaths(cp, SetTo, 1200, " `UniqueCoolTime");
         SetDeaths(cp, SetTo, 120, " `UniqueSkill");
         f.SkillEnd(cp);
      }
   }
}